from environs import Env

env = Env()
env.read_env()
STRIPE_PUBLISHABLE_KEY = env.str('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env.str('STRIPE_SECRET_KEY')
