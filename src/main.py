"""
AI Cost Calculator - Main Entry Point
A tool for estimating AI project costs across multiple categories.
"""

import tkinter as tk
import tkinter.ttk as ttk


class AICostEstimator:
    """Main application class for the AI Cost Estimator."""
    
    def __init__(self):
        """Initialize the main application window."""
        # Initialize main root window with title "AI Cost Estimator"
        self.root = tk.Tk()
        self.root.title("AI Cost Estimator")
        
        # Configure window size and make it resizable
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Configure the main Grid Layout (3 Columns, 3 Rows) with weight/resizing logic
        self.setup_grid_layout()
        
        # Initialize UI components (placeholder for now)
        self.setup_ui_components()
    
    def setup_grid_layout(self):
        """Configure the main grid layout with proper weights for resizing."""
        # Configure 3 columns with different weights
        self.root.columnconfigure(0, weight=1)  # Left panel (Component Builder)
        self.root.columnconfigure(1, weight=2)  # Center panel (Shopping Cart) 
        self.root.columnconfigure(2, weight=1)  # Right panel (Advisory/Totals)
        
        # Configure 3 rows 
        self.root.rowconfigure(0, weight=0)  # Header row (fixed height)
        self.root.rowconfigure(1, weight=1)  # Main content row (expandable)
        self.root.rowconfigure(2, weight=0)  # Footer row (fixed height)
    
    def setup_ui_components(self):
        """Set up the initial UI components (placeholder labels for now)."""
        # Header
        header_label = tk.Label(
            self.root, 
            text="AI Cost Estimator", 
            font=("Arial", 16, "bold"),
            bg="lightblue",
            pady=10
        )
        header_label.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        
        # Left Panel Placeholder
        left_frame = tk.LabelFrame(self.root, text="Component Builder", font=("Arial", 12, "bold"))
        left_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        left_placeholder = tk.Label(left_frame, text="Stack Builder UI\n(Coming Next)", justify=tk.CENTER)
        left_placeholder.pack(expand=True)
        
        # Center Panel Placeholder  
        center_frame = tk.LabelFrame(self.root, text="Shopping Cart", font=("Arial", 12, "bold"))
        center_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        center_placeholder = tk.Label(center_frame, text="Treeview Shopping Cart\n(Coming Next)", justify=tk.CENTER)
        center_placeholder.pack(expand=True)
        
        # Right Panel Placeholder
        right_frame = tk.LabelFrame(self.root, text="Advisory & Totals", font=("Arial", 12, "bold"))
        right_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        right_placeholder = tk.Label(right_frame, text="Dependency Warnings\n+\nTotal Costs\n(Coming Next)", justify=tk.CENTER)
        right_placeholder.pack(expand=True)
        
        # Footer
        footer_label = tk.Label(
            self.root,
            text="Ready to build AI cost estimates",
            bg="lightgray",
            pady=5
        )
        footer_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
    
    def run(self):
        """Start the main application loop."""
        print("AI Cost Calculator - UI Starting...")
        self.root.mainloop()


def main():
    """Main application entry point."""
    app = AICostEstimator()
    app.run()


if __name__ == "__main__":
    main()
