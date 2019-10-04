# Tag Re-Key To Retain History

**Background:**

As part of the conversion of V3 Wellkeeper Sites to nTERFACE and more specifically from the old Wellkeeper V2 push system
to the V3 polling system, the tag names are changed when a site is converted to poll from push.

When the tag name changes all the history for the site that was accumulated through the V2 Bridge is lost which is acceptable
from some operators and not for others. Thus there is a need to "recover" the history and make it available for both
Wellkeeper V3 and to move into nTERFACE.

**Additional Information:**

All of the tag reading data is stored in AWS DynamoDB and is keyed by two items:
- Tag name (example:  PBRPC_Glass_Mtn.M221.TOWER_TEMPERATURE)
- Time Stamp (unix time stamp - seconds since epoc  Example: 1431401090)

And contains:
- Error code (string usually 0)
- Value (string:  72.4046859741)

Here is a JSON object representation:

```
{
  "error": "0",
  "measurement_tag_id": "PBRPC_Glass_Mtn.M221.TOWER_TEMPERATURE",
  "timestamp": 1568769519,
  "value": "72.4046859741"
}
```


**Utility:**

Designed to run from command line within the Wellkeeper AWS VPC environment.  Will require a simple text file with mappings of old-tag-name to new-tag-name (one per line pipe "|" separated) passed on command line.  Example of file contents:

```
1404.41725.1|PBRPC_Glass_Mtn.M221.TOWER_TEMPERATURE
1404.41724.1|PBRPC_Glass_Mtn.M221.BEACON_BULB_STATUS
```


**Usage:**

reKeyTags --help 

**Project Information:**

Put on hold, may not be needed, after discussion with Drake Z, the object is to simply export all the readings
in DynamoDB out to some other format that can be utilized in a more local manner.  Investigating AWS Pipeline
will be closing this feature for now (9/27/19)