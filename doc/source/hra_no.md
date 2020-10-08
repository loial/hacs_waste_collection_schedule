# Hadeland og Ringerike Avfallsselskap AS

Support for schedules provided by [hra.no](https://hra.no/).

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: hra_no
      args:
        agreement: AGREEMENTGUID
```

### Configuration Variables

**agreement**<br>
*(string) (required)*

## Example

```yaml
waste_collection_schedule:
  sources:
    - name: hra_no
      args:
        agreement: ****************
```

## How to get the source arguments

There is a script with an interactive command line interface which generates the required source configuration:

[https://github.com/mampfes/hacs_waste_collection_schedule/blob/master/custom_components/waste_collection_schedule/package/wizard/hra_no.py](https://github.com/mampfes/hacs_waste_collection_schedule/blob/master/custom_components/waste_collection_schedule/package/wizard/hra_no.py).

Just run this script from a shell and answer the questions.
