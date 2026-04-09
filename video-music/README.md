# XLS to XLSX Converter

This tool batch converts Excel `.xls` files to `.xlsx`.

## Usage

1. Put your `.xls` files in a folder.
2. Run the converter:

```bash
./convert_xls_to_xlsx.py ./videos --recursive
```

## EXE Build

- Local Windows build: run `build_windows_exe.bat`
- GitHub Actions build: push a version tag like `v1.2.3`

## Notes

- Always keep a backup before mass conversion.
- `.xlsx` does not preserve VBA macros from `.xls`; use `.xlsm` if macros are required.
