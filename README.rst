easywatch
=========

.. image:: https://badge.fury.io/py/easywatch.png
    :target: http://badge.fury.io/py/easywatch

.. image:: https://pypip.in/d/easywatch/badge.png
        :target: https://crate.io/packages/easywatch/

Dead-simple way to watch a directory.

.. code-block:: python

    import easywatch

    if __name__ == "__main__":
        def handler(event_type, src_path):
            print event_type
            print src_path
        easywatch.watch(".", handler)

Installation
------------

To install easywatch, simply:

.. code-block:: bash

    $ pip install easywatch

Documentation
-------------

Documentation is available at https://github.com/Ceasar/easywatch/tree/master/docs

Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/Ceasar/easywatch
.. _AUTHORS: https://github.com/Ceasar/easywatch/blob/master/AUTHORS.rst
