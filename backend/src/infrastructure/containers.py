from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.infrastructure.api.routes",
        ]
    )

    int_provider = providers.Factory(lambda: 1)
