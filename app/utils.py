import functools

from flask import render_template


def uses_template(template):
    """Wrap a function to add HTML template rendering functionality."""
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            template_path = template
            ctx = func(*args, **kwargs)
            if type(ctx) is dict:
                try:
                    return render_template(template_path,
                                           veteran=ctx['veteran'])
                except KeyError:
                    try:
                        return render_template(template_path,
                                               organization=ctx['organization']
                                               )
                    except KeyError:
                        return render_template(template_path,
                                               posts=ctx['posts'])
            else:
                return ctx
        return wrapped
    return wrapper
