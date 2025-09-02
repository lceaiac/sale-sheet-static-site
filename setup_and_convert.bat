@echo off
echo ========================================
echo Cannabis Sales Sheet PDF Converter
echo ========================================
echo.

echo Checking Python installation...
py --version >nul 2>&1
if %errorlevel% neq 0 (
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ERROR: Python is not installed or not in PATH
        echo Please install Python from https://python.org
        echo.
        echo ALTERNATIVE: You can use the browser-based converter!
        echo Opening browser converter...
        start browser_pdf_converter.html
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo Python found! Installing required packages...
echo.

echo Installing weasyprint...
%PYTHON_CMD% -m pip install weasyprint
if %errorlevel% neq 0 (
    echo WARNING: Failed to install weasyprint
    echo This is common on Windows due to system library dependencies.
    echo.
    echo Trying alternative method with pdfkit...
    %PYTHON_CMD% -m pip install pdfkit
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install pdfkit as well
        echo.
        echo SOLUTION: Use the browser-based converter instead!
        echo Opening browser converter...
        start browser_pdf_converter.html
        pause
        exit /b 1
    )
    echo pdfkit installed successfully!
    echo Note: You may need to install wkhtmltopdf separately
    echo Download from: https://wkhtmltopdf.org/downloads.html
    echo.
    echo Trying alternative converter...
    %PYTHON_CMD% html_to_pdf_alternative.py
    goto :check_result
)

echo Installing Pillow...
%PYTHON_CMD% -m pip install Pillow
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Pillow
    echo Opening browser converter as fallback...
    start browser_pdf_converter.html
    pause
    exit /b 1
)

echo.
echo All dependencies installed successfully!
echo.
echo Converting HTML to PDF...
echo.

%PYTHON_CMD% html_to_pdf_converter.py

:check_result
if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Conversion completed successfully!
    echo ========================================
    echo.
    echo The PDF file has been created in the same directory.
    echo You can now print or share the single-page PDF.
) else (
    echo.
    echo ========================================
    echo Python conversion failed!
    echo ========================================
    echo.
    echo Don't worry! Opening the browser-based converter...
    echo This method works on any system without additional software.
    start browser_pdf_converter.html
)

echo.
echo Press any key to exit...
pause >nul