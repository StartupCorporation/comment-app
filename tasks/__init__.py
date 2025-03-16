from invoke.collection import Collection

from deps import collection


namespace = Collection()
namespace.add_collection(
    coll=collection,
    name="deps",
)
