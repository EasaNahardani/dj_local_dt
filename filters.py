###################
# DATES           #
###################

@register.filter(expects_localtime=True, is_safe=False)
def date(value, arg=None):
    """Format a date according to the given format."""
    if value in (None, ''):
        return ''
    try:
        return formats.date_format(value, arg)
    except AttributeError:
        try:
            return format(value, arg)
        except AttributeError:
            return ''


@register.filter(expects_localtime=True, is_safe=False)
def time(value, arg=None):
    """Format a time according to the given format."""
    if value in (None, ''):
        return ''
    try:
        return formats.time_format(value, arg)
    except (AttributeError, TypeError):
        try:
            return time_format(value, arg)
        except (AttributeError, TypeError):
            return ''


@register.filter("timesince", is_safe=False)
def timesince_filter(value, arg=None):
    """Format a date as the time since that date (i.e. "4 days, 6 hours")."""
    if not value:
        return ''
    try:
        if arg:
            return timesince(value, arg)
        return timesince(value)
    except (ValueError, TypeError):
        return ''


@register.filter("timeuntil", is_safe=False)
def timeuntil_filter(value, arg=None):
    """Format a date as the time until that date (i.e. "4 days, 6 hours")."""
    if not value:
        return ''
    try:
        return timeuntil(value, arg)
    except (ValueError, TypeError):
        return ''
