easywatch
=========

Dead-simple way to watch a directory.

Installation
------------

`pip install easywatch`

Quickstart
----------

`easywatch` has just one function, `watch` which watches a directory for changes and notifies a handler the type of event and the name of the file that triggered it.

There are four types of events that the handler can be notified about:

-   `created` - a file was created
-   `deleted` - a file was deleted
-   `modified` - a file was modified
-   `moved` - a file was moved

For instance:

```python
import easywatch

if __name__ == "__main__":
    def handler(event_type, src_path):
        print event_type
        print src_path
    easy.watch(".", handler)
```

Note that `src_path` is just the absolute path to the file.

And that's pretty much it. If you need more customization, check out `watchdog`, which `easywatch` wraps.
