# Python Publix BOGO

## Overview

Get a list of the weekly BOGO's at Publix.

## Installation

```bash
TODO
```

## Usage

```python
from pypublixbogo.pypublixbogo import PublixBogo


PALM_CROSSINGS = 2500579

bogo_data = PublixBogo(store_number=PALM_CROSSINGS)

# Get the date.
date = bogo_data.get_date()

# Get a modified cleaned up version of the date.
custom_date = bogo_data.get_modified_date()

# Get a list of all the BOGO's for the week.
bogo_items = _bogo_data.get_bogo_items()

```

## References
