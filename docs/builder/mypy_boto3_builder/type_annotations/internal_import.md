# InternalImport

> Auto-generated documentation for [builder.mypy_boto3_builder.type_annotations.internal_import](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / InternalImport
    - [InternalImport](#internalimport)
        - [InternalImport().get_import_record](#internalimportget_import_record)
        - [InternalImport().localize](#internalimportlocalize)
        - [InternalImport().render](#internalimportrender)
        - [InternalImport().scope](#internalimportscope)

## InternalImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L9)

```python
class InternalImport(FakeAnnotation):
    def __init__(
        name: str,
        service_name: ServiceName,
        module_name: str = 'service_resource',
    ) -> None:
```

### InternalImport().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L33)

```python
def get_import_record() -> ImportRecord:
```

### InternalImport().localize

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L30)

```python
def localize(service_name: ServiceName) -> None:
```

### InternalImport().render

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L23)

```python
def render() -> str:
```

### InternalImport().scope

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/type_annotations/internal_import.py#L26)

```python
@property
def scope() -> str:
```
