from typing import Callable, Awaitable, Sequence

from infrastructure.bus.command.handler import CommandHandler
from infrastructure.bus.command.message import Command
from infrastructure.bus.middleware.base import BusMiddleware


class CommandBus:
    def __init__(
        self,
        middlewares: Sequence[BusMiddleware] | None = None,
    ):
        self._handlers: dict[type[Command], CommandHandler] = {}
        self._middleware_chain: Callable[[Command], Awaitable[None]] = self._build_middleware_chain(
            middlewares=middlewares or [],
        )

    def register(
        self,
        command: type[Command],
        handler: CommandHandler,
    ) -> None:
        self._handlers[command] = handler

    async def handle(
        self,
        command: Command,
    ) -> None:
        await self._middleware_chain(command)

    def _build_middleware_chain(
        self,
        middlewares: Sequence[BusMiddleware],
    ) -> Callable[[Command], Awaitable[None]]:
        async def command_executor(command: Command) -> None:
            command_handler = self._handlers.get(command.__class__)

            if not command_handler:
                raise ValueError(f"Command handler doesn't exist for the '{command.__class__}' command")

            await command_handler(command=command)

        def wrapped_middleware(
            middleware: BusMiddleware,
            next_handler: Callable[[Command], Awaitable[None]],
        ) -> Callable[[Command], Awaitable[None]]:
            async def wrapped_handler(command: Command) -> None:
                return await middleware(
                    message=command,
                    next_=next_handler,
                )

            return wrapped_handler

        for mdl in middlewares[::-1]:
            command_executor = wrapped_middleware(  # type: ignore
                middleware=mdl,
                next_handler=command_executor,
            )

        return command_executor
