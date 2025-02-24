from domain.comment.repository import CommentRepository
from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.middleware.transaction import TransactionMiddleware
from infrastructure.bus.query.bus import QueryBus
from infrastructure.database.base.transaction import DatabaseTransactionManager
from infrastructure.database.relational.connection import SQLDatabaseConnectionManager
from infrastructure.database.relational.mapper import DatabaseToEntityMapper
from infrastructure.database.relational.repository.comment import SQLAlchemyCommentRepository
from infrastructure.database.relational.transaction import SQLDatabaseTransactionManager
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer
from infrastructure.settings.application import ApplicationSettings
from infrastructure.settings.database import DatabaseSettings


class InfrastructureLayer(Layer):
    def setup(
        self,
        container: Container,
    ) -> None:
        container[ApplicationSettings] = ApplicationSettings()  # type: ignore
        container[DatabaseSettings] = DatabaseSettings()  # type: ignore

        container[SQLDatabaseConnectionManager] = SQLDatabaseConnectionManager(
            settings=container[DatabaseSettings],
        )
        container[DatabaseTransactionManager] = SQLDatabaseTransactionManager(
            connection_manager=container[SQLDatabaseConnectionManager],
        )
        container[TransactionMiddleware] = TransactionMiddleware(
            transaction_manager=container[DatabaseTransactionManager],
        )

        container[CommentRepository] = SQLAlchemyCommentRepository(
            connection_manager=container[SQLDatabaseConnectionManager],
        )

        container[QueryBus] = QueryBus()
        container[CommandBus] = CommandBus(
            middlewares=(container[TransactionMiddleware],),
        )

        container[DatabaseToEntityMapper] = DatabaseToEntityMapper()

        self._run_entity_to_database_mapping(
            mapper=container[DatabaseToEntityMapper],
        )

    @staticmethod
    def _run_entity_to_database_mapping(mapper: DatabaseToEntityMapper):
        mapper.map()
