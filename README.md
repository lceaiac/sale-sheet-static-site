# Cannabis Sales Sheet PDF Converter

This project provides scripts to convert the cannabis sales sheet HTML document into a single-page PDF file, ensuring all content is properly scaled and formatted to fit within one page without any overflow or loss of information.

## 📁 Files Overview

- `sales_sheetv1.html` - Original HTML sales sheet
- `browser_pdf_converter.html` - **Browser-based converter (RECOMMENDED)**
- `html_to_pdf_converter.py` - Main converter using WeasyPrint
- `html_to_pdf_alternative.py` - Alternative converter using pdfkit
- `setup_and_convert.bat` - Windows batch script for easy setup and conversion
- `convert_to_pdf.ps1` - PowerShell script with multiple conversion methods
- `README.md` - This documentation file

## 🚀 Quick Start

### Method 1: Browser-Based Converter (RECOMMENDED - No Installation Required)

1. **Double-click `browser_pdf_converter.html`**
2. **Follow the step-by-step instructions** in your browser
3. **Use your browser's print function** to save as PDF
4. **Adjust scale to 85-90%** to fit everything on one page

✅ **Advantages:**
- Works on any operating system
- No software installation required
- Uses your browser's built-in PDF engine
- Always works regardless of system configuration

### Method 2: Automated Setup (Windows)

1. **Double-click `setup_and_convert.bat`**
2. The script will automatically:
   - Check for Python installation
   - Install required packages
   - Convert the HTML to PDF
   - Fall back to browser method if Python fails

### Method 3: PowerShell Script (Windows)

1. **Right-click `convert_to_pdf.ps1`** and select "Run with PowerShell"
2. The script will try multiple conversion methods automatically

### Method 4: Manual Python Setup

1. **Install Python** (if not already installed)
   - Download from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH" during installation

2. **Install required packages**
   ```bash
   pip install weasyprint Pillow
   ```

3. **Run the converter**
   ```bash
   python html_to_pdf_converter.py
   ```

## 🔧 Alternative Method (if WeasyPrint fails)

If the main converter doesn't work, try the alternative method:

1. **Install pdfkit**
   ```bash
   pip install pdfkit
   ```

2. **Install wkhtmltopdf**
   - Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
   - Install and make sure it's in your system PATH

3. **Run the alternative converter**
   ```bash
   python html_to_pdf_alternative.py
   ```

## 📄 Output Files

- **Browser method:** You choose the filename when saving
- `cannabis_sales_sheet_single_page.pdf` - PDF created by main Python converter
- `cannabis_sales_sheet_single_page_alt.pdf` - PDF created by alternative Python converter

## ✨ Features

### Single-Page Layout
- **Automatic Scaling**: All content is automatically scaled to fit on one A4 page
- **Grid Optimization**: Products are arranged in a 4-column grid for maximum space efficiency
- **Font Scaling**: Text sizes are optimized for readability while maintaining information density
- **Image Optimization**: Product images are resized to maintain visual appeal without taking excessive space

### Content Preservation
- **Complete Information**: All product details, prices, and specifications are preserved
- **Visual Hierarchy**: Important information like prices and THC content remain prominent
- **Brand Identity**: Logo and branding elements are maintained
- **QR Code**: Order and contact QR code is included and properly sized

### Print Optimization
- **A4 Paper Size**: Optimized for standard 8.5" x 11" paper
- **Proper Margins**: Ensures content doesn't get cut off when printing
- **High Quality**: Vector graphics and text remain crisp when printed
- **Professional Layout**: Maintains the professional appearance of the original design

## 🎯 Why Browser Method is Recommended

### Universal Compatibility
- **No Dependencies:** Works without installing Python or additional libraries
- **Cross-Platform:** Works on Windows, Mac, Linux, and mobile devices
- **Always Updated:** Uses your browser's latest PDF engine
- **No Errors:** Eliminates common Python/library installation issues

### Professional Results
- **High Quality:** Modern browsers produce excellent PDF output
- **Accurate Rendering:** Perfect CSS and image handling
- **Consistent Results:** Same output across different systems
- **Print Optimization:** Built-in print CSS is automatically applied

### User-Friendly
- **Visual Control:** See exactly what will be in your PDF
- **Real-time Adjustment:** Adjust scale and margins in print preview
- **Familiar Interface:** Uses standard browser print dialog
- **Immediate Results:** No waiting for processing or installations

## 🛠️ Technical Details

### Main Converter (WeasyPrint)
- Uses WeasyPrint engine for HTML to PDF conversion
- Applies custom CSS for single-page layout
- Handles fonts and styling accurately
- Better support for modern CSS features

### Alternative Converter (pdfkit)
- Uses wkhtmltopdf engine via pdfkit
- Injects additional CSS for layout optimization
- Good fallback option if WeasyPrint has issues
- Requires separate wkhtmltopdf installation

### CSS Optimizations Applied
- Font sizes reduced to 4-7px range for content density
- Grid layout changed to 4 columns for better space utilization
- Margins and padding minimized throughout
- Image heights reduced to 55-60px
- Transform scaling applied for fine-tuning

## 🔍 Troubleshooting

### Common Issues

**"Python is not installed or not in PATH"**
- Install Python from python.org
- Make sure to check "Add Python to PATH" during installation
- Restart your command prompt/terminal after installation

**"weasyprint installation failed"**
- Try installing Visual C++ Build Tools
- Use the alternative converter instead
- On some systems, try: `pip install --only-binary=all weasyprint`

**"wkhtmltopdf not found"**
- Download and install wkhtmltopdf from the official website
- Make sure the installation directory is added to your system PATH
- Restart your command prompt after installation

**"Images not showing in PDF"**
- Make sure all image files (PNG) are in the same directory as the HTML file
- Check that image file names match exactly (case-sensitive)

**"Content is cut off or too small"**
- The scripts are optimized for A4 paper size
- If using different paper size, you may need to adjust the CSS scaling values
- Try printing at 100% scale (not "Fit to page")

### Getting Help

If you encounter issues:
1. Check that all image files are present in the directory
2. Ensure Python and pip are properly installed
3. Try the alternative converter if the main one fails
4. Check the console output for specific error messages

## 📋 Requirements

### System Requirements
- Windows 10 or later (scripts can be adapted for Mac/Linux)
- Python 3.7 or later
- Internet connection for package installation

### Python Packages
- **weasyprint**: For main converter
- **Pillow**: Image processing support
- **pdfkit**: For alternative converter (optional)

### External Tools
- **wkhtmltopdf**: Required only for alternative converter

## 📝 Customization

To modify the layout or styling:

1. **Font Sizes**: Edit the CSS values in the converter scripts
2. **Grid Layout**: Change `grid-template-columns` value (currently set to 4 columns)
3. **Margins**: Adjust the `@page` margin values
4. **Image Sizes**: Modify the height values for `.product-image` and `.flower-image`

## 📞 Support

For technical support or questions about the cannabis products:
- Email: david@honestpharmco.com
- Phone: 585-519-9778

---

*This converter ensures your cannabis sales sheet maintains its professional appearance while being optimized for single-page printing and distribution.*