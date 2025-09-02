#!/usr/bin/env python3
"""
Automated HTML to Single-Page PDF Converter
This script uses Playwright to automate browser PDF generation
"""

import os
import sys
from pathlib import Path

def install_playwright():
    """Install playwright and browser if not available"""
    try:
        import playwright
        print("✅ Playwright already installed")
        return True
    except ImportError:
        print("📦 Installing Playwright...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
            subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
            print("✅ Playwright installed successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to install Playwright: {e}")
            return False

def convert_html_to_pdf_automated(html_file, output_pdf):
    """Convert HTML to PDF using automated browser"""
    try:
        from playwright.sync_api import sync_playwright
        
        print(f"🔄 Converting {html_file} to {output_pdf}...")
        
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Navigate to HTML file
            html_path = Path(html_file).resolve().as_uri()
            page.goto(html_path)
            
            # Wait for page to load completely
            page.wait_for_load_state('networkidle')
            
            # Generate PDF with optimized settings for single page
            page.pdf(
                path=output_pdf,
                format='A4',
                print_background=True,
                margin={
                    'top': '0.2in',
                    'right': '0.2in', 
                    'bottom': '0.2in',
                    'left': '0.2in'
                },
                scale=0.85,  # Scale to fit content on one page
                prefer_css_page_size=False
            )
            
            browser.close()
            
        print(f"✅ PDF successfully created: {output_pdf}")
        return True
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        return False

def main():
    """Main conversion function"""
    print("")
    print("========================================")
    print("   Automated HTML to PDF Converter     ")
    print("========================================")
    print("")
    
    # Define file paths
    html_file = "sales_sheetv1.html"
    output_pdf = "cannabis_sales_sheet_automated.pdf"
    
    # Check if HTML file exists
    if not os.path.exists(html_file):
        print(f"❌ Error: {html_file} not found!")
        print("Please make sure the HTML file is in the current directory.")
        return False
    
    print(f"📄 Input HTML: {html_file}")
    print(f"📄 Output PDF: {output_pdf}")
    print("")
    
    # Install Playwright if needed
    if not install_playwright():
        print("❌ Cannot proceed without Playwright")
        return False
    
    print("")
    
    # Convert HTML to PDF
    success = convert_html_to_pdf_automated(html_file, output_pdf)
    
    print("")
    print("========================================")
    if success:
        print("   Conversion Completed Successfully!   ")
        print(f"📄 PDF created: {output_pdf}")
    else:
        print("   Conversion Failed                    ")
    print("========================================")
    print("")
    
    return success

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ Conversion cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)