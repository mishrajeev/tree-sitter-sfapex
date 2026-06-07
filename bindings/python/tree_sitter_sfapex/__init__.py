from ._binding import language_apex as _language_apex
from ._binding import language_soql as _language_soql
from ._binding import language_sosl as _language_sosl
from ._binding import language_sflog as _language_sflog
from tree_sitter import Language


def language_apex() -> Language:
    """Return the tree-sitter Language object for Apex."""
    return Language(_language_apex())


def language_soql() -> Language:
    """Return the tree-sitter Language object for SOQL."""
    return Language(_language_soql())


def language_sosl() -> Language:
    """Return the tree-sitter Language object for SOSL."""
    return Language(_language_sosl())


def language_sflog() -> Language:
    """Return the tree-sitter Language object for Salesforce debug log."""
    return Language(_language_sflog())
