from management.commands import clear_data as clr


def clean_upvotes_every_day():
    """cleans upvotes in database every day"""
    command = clr.Command()
    command.handle()
