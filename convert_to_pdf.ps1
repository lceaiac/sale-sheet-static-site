# HTML to PDF Converter - Multiple Methods
# This script tries different conversion methods automatically

Write-Host "" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "   HTML to Single-Page PDF Converter   " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Define file paths
$htmlFile = "sales_sheetv1.html"
$outputPdf1 = "cannabis_sales_sheet_single_page.pdf"
$outputPdf2 = "cannabis_sales_sheet_single_page_alt.pdf"
$browserConverter = "browser_pdf_converter.html"

# Check if HTML file exists
if (-not (Test-Path $htmlFile)) {
    Write-Host "Error: $htmlFile not found!" -ForegroundColor Red
    Write-Host "Please make sure the HTML file is in the current directory." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host "Found HTML file: $htmlFile" -ForegroundColor Green
Write-Host ""

# Function to check if Python is available
function Test-Python {
    try {
        $pythonVersion = & py --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Python found: $pythonVersion" -ForegroundColor Green
            return "py"
        }
    } catch {}
    
    try {
        $pythonVersion = & python --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Python found: $pythonVersion" -ForegroundColor Green
            return "python"
        }
    } catch {}
    
    Write-Host "Python not found or not in PATH" -ForegroundColor Yellow
    return $null
}

# Function to try WeasyPrint converter
function Try-WeasyPrintConverter {
    param($pythonCmd)
    
    Write-Host "Attempting conversion with WeasyPrint..." -ForegroundColor Cyan
    try {
        & $pythonCmd "html_to_pdf_converter.py"
        if ($LASTEXITCODE -eq 0 -and (Test-Path $outputPdf1)) {
            Write-Host "Success! PDF created: $outputPdf1" -ForegroundColor Green
            return $true
        }
    } catch {
        Write-Host "WeasyPrint conversion failed: $($_.Exception.Message)" -ForegroundColor Red
    }
    return $false
}

# Function to try pdfkit converter
function Try-PdfkitConverter {
    param($pythonCmd)
    
    Write-Host "Attempting conversion with pdfkit..." -ForegroundColor Cyan
    
    # Install pdfkit if needed
    Write-Host "Installing pdfkit..." -ForegroundColor Yellow
    & $pythonCmd "-m" "pip" "install" "pdfkit" 2>$null
    
    try {
        & $pythonCmd "html_to_pdf_alternative.py"
        if ($LASTEXITCODE -eq 0 -and (Test-Path $outputPdf2)) {
            Write-Host "Success! PDF created: $outputPdf2" -ForegroundColor Green
            return $true
        }
    } catch {
        Write-Host "pdfkit conversion failed: $($_.Exception.Message)" -ForegroundColor Red
    }
    return $false
}

# Function to open browser converter
function Open-BrowserConverter {
    Write-Host "Opening browser-based converter..." -ForegroundColor Cyan
    Write-Host "This will open a webpage with step-by-step instructions." -ForegroundColor Yellow
    Write-Host ""
    
    if (Test-Path $browserConverter) {
        try {
            Start-Process $browserConverter
            Write-Host "Browser converter opened successfully!" -ForegroundColor Green
            Write-Host "Follow the instructions in your browser to convert to PDF." -ForegroundColor Yellow
            return $true
        } catch {
            Write-Host "Failed to open browser converter: $($_.Exception.Message)" -ForegroundColor Red
        }
    } else {
        Write-Host "Browser converter file not found: $browserConverter" -ForegroundColor Red
    }
    return $false
}

# Main conversion logic
$pythonCmd = Test-Python
$conversionSuccess = $false

if ($pythonCmd) {
    Write-Host "Trying Python-based converters..." -ForegroundColor Cyan
    Write-Host ""
    
    # Try WeasyPrint first
    if (Try-WeasyPrintConverter $pythonCmd) {
        $conversionSuccess = $true
    }
    # If WeasyPrint fails, try pdfkit
    elseif (Try-PdfkitConverter $pythonCmd) {
        $conversionSuccess = $true
    }
}

# If Python methods failed or Python not available, use browser method
if (-not $conversionSuccess) {
    Write-Host ""
    Write-Host "Python conversion methods unavailable or failed." -ForegroundColor Yellow
    Write-Host "Falling back to browser-based conversion..." -ForegroundColor Cyan
    Write-Host ""
    
    if (Open-BrowserConverter) {
        $conversionSuccess = $true
    }
}

# Final status
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
if ($conversionSuccess) {
    Write-Host "   Conversion Process Completed!        " -ForegroundColor Green
} else {
    Write-Host "   Conversion Process Failed            " -ForegroundColor Red
}
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

if (-not $conversionSuccess) {
    Write-Host "Manual Instructions:" -ForegroundColor Yellow
    Write-Host "1. Open $htmlFile in your web browser" -ForegroundColor White
    Write-Host "2. Press Ctrl+P to print" -ForegroundColor White
    Write-Host "3. Choose 'Save as PDF' as destination" -ForegroundColor White
    Write-Host "4. Set scale to 85-90% to fit on one page" -ForegroundColor White
    Write-Host "5. Set margins to 'Minimum'" -ForegroundColor White
    Write-Host "6. Click 'Save'" -ForegroundColor White
    Write-Host ""
}

Write-Host "Support: david@honestpharmco.com | 585-519-9778" -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")