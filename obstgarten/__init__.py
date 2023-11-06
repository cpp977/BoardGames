from gymnasium.envs.registration import register

register(
    id="obstgarten/GridWorld-v0",
    entry_point="obstgarten.envs:GridWorldEnv",
)
