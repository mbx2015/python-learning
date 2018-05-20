import argparse

parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description="""
                                    description
                                        not
                                            wrapped""",
                                 epilog="""
                                    epilog
                                        not
                                            wrapped""",
                                 )
parser.add_argument('-a', action="store_true", help="""argument
                                    help is
                                    wrapped
                                    """, )
parser.print_help()
