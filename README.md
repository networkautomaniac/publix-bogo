# Publix BOGO

## Overview

Get a list of the weekly BOGO's at Publix.  This uses the Publix Accessible Weekly Ad and not the standard ad.

## Usage

```python
from publix_bogo.publix_bogo import PublixBogo

# Palm Crossings Store Number.
PALM_CROSSINGS = 2500579

bogo_data = PublixBogo(store_number=PALM_CROSSINGS)

# Get the date.
date = bogo_data.get_date()
print(date)

# Get a modified cleaned up version of the date.
custom_date = bogo_data.get_modified_date()
print(custom_date)

# Get a list of all the BOGO's for the week.
bogo_items = bogo_data.get_bogo_items()
print(bogo_items)

```

## References

- ### Publix Accessibility Site

  - <https://accessibleweeklyad.publix.com>
