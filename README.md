# subnetter
This simple Python script takes a CIDR range and prefix length as arguments and splits the CIDR into smaller subnets of the specified prefix length.
It can be used for easy port scanning by splitting the scanning process across subnets.

## Usage
```bash
git clone https://github.com/St74nger/subnetter.git
cd subnetter
python3 subnetter.py <CIDR> <prefix>
```
- CIDR is the target CIDR range to split, like 10.0.0.0/16
- prefix is the prefix length for the smaller subnets, like 24 or 20

For example:

```bash
python3 subnetter.py 10.0.0.0/16 24
```
