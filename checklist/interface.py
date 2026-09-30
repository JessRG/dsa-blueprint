import tkinter as tk
from tkinter import ttk
from manager import ChecklistManager


class TkinterInterface:
    """Manages the graphical user interface configuration using grid layout tracking."""

    def __init__(self, manager: ChecklistManager):
        self.manager: ChecklistManager = manager

        # Primary Window Setup
        self.root = tk.Tk()
        self.root.title("LeetCode 12-Week Study Tracker")
        self.root.geometry("750x800")
        self.root.minsize(650, 550)

        # Internal state map tracking Tkinter BooleanVar objects back to flat indices
        self.check_vars = {}

        self._build_styles()
        self._create_widgets()
        self._update_progress_bar()

    def _build_styles(self) -> None:
        """Sets up theme configurations and visual element styling definitions."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TFrame", background="#f5f5f7")
        self.style.configure("Card.TFrame", background="#ffffff", relief="solid", borderwidth=1)
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"), background="#f5f5f7", foreground="#1d1d1f")
        self.style.configure("Week.TLabel", font=("Arial", 12, "bold"), background="#ffffff", foreground="#0071e3")
        self.style.configure("Diff.TLabel", font=("Arial", 10, "bold"), background="#ffffff", foreground="#86868b")

        self.root.configure(background="#f5f5f7")

    def _create_widgets(self) -> None:
        """Assembles components using explicit row and column grid coordinate parameters."""
        # Configure root layout sizing weights
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # --- Top Analytics Panel (Grid Row 0) ---
        self.progress_frame = ttk.Frame(self.root, padding=15, style="TFrame")
        self.progress_frame.grid(row=0, column=0, sticky="ew")
        self.progress_frame.grid_columnconfigure(0, weight=1)

        self.header_label = ttk.Label(self.progress_frame, text="My LeetCode Progress Plan", style="Header.TLabel")
        self.header_label.grid(row=0, column=0, sticky="w")

        self.stats_label = ttk.Label(self.progress_frame, text="0/0 Problems Completed (0.0%)", font=("Arial", 10),
                                     background="#f5f5f7")
        self.stats_label.grid(row=1, column=0, sticky="w", pady=(5, 5))

        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", mode="determinate")
        self.progress_bar.grid(row=2, column=0, sticky="ew")

        # --- Middle Scrollable Container Canvas Workspace (Grid Row 1) ---
        self.outer_container = ttk.Frame(self.root, padding=10, style="TFrame")
        self.outer_container.grid(row=1, column=0, sticky="nsew")
        self.outer_container.grid_rowconfigure(0, weight=1)
        self.outer_container.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.outer_container, bg="#f5f5f7", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.outer_container, orient="vertical", command=self.canvas.yview)

        self.scroll_content = ttk.Frame(self.canvas, style="TFrame")
        self.scroll_content.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_frame_id = self.canvas.create_window((0, 0), window=self.scroll_content, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Grid layout for canvas and scrollbar inside the container view
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.canvas.bind('<Configure>',
                         lambda event: self.canvas.itemconfigure(self.canvas_frame_id, width=event.width))

        # --- Dynamic Checklist Hierarchy Node Generation via Grid ---
        self.scroll_content.grid_columnconfigure(0, weight=1)
        flat_counter = 1
        card_row = 0

        for week in self.manager.weeks:
            week_card = ttk.Frame(self.scroll_content, padding=12, style="Card.TFrame")
            week_card.grid(row=card_row, column=0, sticky="ew", pady=10, padx=5)
            week_card.grid_columnconfigure(0, weight=1)

            week_label = ttk.Label(week_card, text=f"Week {week.week}: {week.topic}", style="Week.TLabel")
            week_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

            item_row = 1
            for category in week.categories:
                diff_label = ttk.Label(week_card, text=f"  {category.difficulty}", style="Diff.TLabel")
                diff_label.grid(row=item_row, column=0, sticky="w", pady=(4, 2))
                item_row += 1

                for problem in category.problems:
                    var = tk.BooleanVar(value=problem.completed)
                    self.check_vars[flat_counter] = var

                    chk = tk.Checkbutton(
                        week_card,
                        text=f"[{flat_counter:3}]  {problem.name}",
                        variable=var,
                        onvalue=True,
                        offvalue=False,
                        bg="#ffffff",
                        activebackground="#ffffff",
                        font=("Arial", 10),
                        anchor="w",
                        command=lambda idx=flat_counter: self._on_checkbox_toggled(idx)
                    )
                    chk.grid(row=item_row, column=0, sticky="w", padx=20, pady=1)
                    flat_counter += 1
                    item_row += 1

            card_row += 1

    def _on_checkbox_toggled(self, flat_index: int) -> None:
        """Fires when any checkbox item widget node captures mouse selection interactions."""
        self.manager.toggle_problem_by_index(flat_index)
        self._update_progress_bar()

    def _update_progress_bar(self) -> None:
        """Pulls global data metrics dynamically to update graphical rendering scales."""
        completed, total, pct = self.manager.get_progress_metrics()
        self.stats_label.config(text=f"{completed}/{total} Problems Completed ({pct:.1f}%)")
        self.progress_bar["value"] = pct

    def start_loop(self) -> None:
        """Starts processing window events inside the main loop."""
        self.root.mainloop()