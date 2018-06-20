Changelog
=========

v0.12
-----

New
~~~

- Supports HALO_API_HOSTNAME for use with non-MTG environments. [Ash
  Wilson]

  This tool defaults to `api.cloudpassage.com` for HALO_API_HOSTNAME.

  Setting this environment variable when running the container
  is only necessary for environments which are not in the
  CloudPassage MTG.

  This commit also includes a refactor of the GetEvents() class,
  which now uses the TimeSeries() abstraction in the Python SDK
  instead of the halo-events library.

  Closes #4

Changes
~~~~~~~

- Target date defaults to yesterday. [Ash Wilson]

  If no TARGET_DATE is specified, the prior day is set.

  Supports HALO_API_HOSTNAME environment variable.

  Closes #4

v0.10 (2017-03-31)
------------------

Changes
~~~~~~~

- Auto-adjusts retrieval intensity based on event generation frequency.
  [Ash Wilson]

v0.9 (2016-12-19)
-----------------

New
~~~

- Downloads all events for a given day.  Optionally uploads to an S3
  bucket. [Ash Wilson]


