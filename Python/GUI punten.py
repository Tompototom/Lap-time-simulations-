# fs_gui.py — GUI with t_ref inputs + startup popup (functions unchanged)

import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- YOUR FUNCTIONS (DO NOT EDIT) --------------------
def acceleration_score(t_team: float) -> float:
    P_max, T_max = 50, 1.5 * 3.454
    t = min(t_team, T_max)
    raw = ((T_max / t) - 1) / 0.5
    res = 0.95 * P_max * raw + 0.05 * P_max
    ret = min(P_max, res)
    return ret

def skidpad_score(t_team: float) -> float:
    t_team = t_team/2
    
    P_max = 50 
    T_max = 1.25 * 4.627 #2024 fastest time FSG
    t = min(t_team, T_max)
    raw = ((((T_max / t) ** 2) - 1) / 0.5625)
    res = 0.95 * P_max * raw + 0.05 * P_max
    ret = min(P_max, res)
    return ret

def autocross_score(t_team: float) -> float:
    P_max, T_max = 100, 1.25 * 75.93
    t = min(t_team, T_max)
    frac = (T_max / t) - 1
    term = frac / 0.25 if frac > 0 else 0
    res = 0.95 * P_max * term + 0.05 * P_max
    ret = min(P_max, res)
    return ret

def endurance_score(t_lap: float) -> float:
    P_max, T_max = 250, 1.333 * 1420.56
    T_team = 18 * t_lap
    t = min(T_team, T_max)
    raw = ((T_max / t) - 1) / 0.333
    res = 0.90 * P_max * raw + 0.10 * P_max
    ret = min(P_max, res)
    return ret
# ----------------------------------------------------------------------

# t_ref defaults
ACC_TREF_DEF = 3.388  #2024 FSG reference time
SKP_TREF_DEF = 4.627    #2024 FSG reference time
AX_TREF_DEF  = 75.933    # 2012 FSG reference time 
END_TREF_DEF = 1420.56   #2012 FSG reference time

# Factors producing T_max = factor * t_ref
ACC_FACTOR = 1.5
SKP_FACTOR = 1.25
AX_FACTOR  = 1.25
END_FACTOR = 1.333

# The T_max values hardcoded inside your functions (keep as constants)
ACC_TMAX_DEF = ACC_FACTOR * ACC_TREF_DEF
SKP_TMAX_DEF = SKP_FACTOR * SKP_TREF_DEF
AX_TMAX_DEF  = AX_FACTOR  * AX_TREF_DEF
END_TMAX_DEF = END_FACTOR * END_TREF_DEF

INFO_MESSAGE = (
    "The standard ref times for Acceleration and skidpad are from the 2024 FSG "
    "while the Endurance and autocross are from the 2012 FSG"
)

def f2(x: float) -> str:
    return f"{x:.2f}"

def scale_for_new_tmax(t_in: float, tmax_def: float, tmax_new: float) -> float:
    # Ensures (T_max_def / t_scaled) == (T_max_new / t_original)
    return t_in * (tmax_def / tmax_new)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FS Scores — t_ref inputs (functions unchanged)")
        self.resizable(False, False)
        pad = {"padx": 8, "pady": 6}
        ttk.Style().configure("Hdr.TLabel", font=("Segoe UI", 11, "bold"))

        # Acceleration
        ttk.Label(self, text="Acceleration", style="Hdr.TLabel").grid(row=0, column=0, sticky="w", **pad)
        ttk.Label(self, text="t_team [s]").grid(row=0, column=1, sticky="e", **pad)
        self.acc_t = tk.StringVar(); ttk.Entry(self, textvariable=self.acc_t, width=10).grid(row=0, column=2, **pad)
        ttk.Label(self, text="t_ref [s]").grid(row=0, column=3, sticky="e", **pad)
        self.acc_ref = tk.StringVar(value=f2(ACC_TREF_DEF)); ttk.Entry(self, textvariable=self.acc_ref, width=10).grid(row=0, column=4, **pad)
        ttk.Label(self, text="(×1.5)").grid(row=0, column=5, sticky="w", **pad)
        self.acc_out = tk.StringVar(value="-"); ttk.Label(self, textvariable=self.acc_out).grid(row=0, column=6, **pad)

        # Skidpad
        ttk.Label(self, text="Skidpad (t_team = 2 laps total)", style="Hdr.TLabel").grid(row=1, column=0, sticky="w", **pad)
        ttk.Label(self, text="t_team total [s]").grid(row=1, column=1, sticky="e", **pad)
        self.skp_t = tk.StringVar(); ttk.Entry(self, textvariable=self.skp_t, width=10).grid(row=1, column=2, **pad)
        ttk.Label(self, text="t_ref [s]").grid(row=1, column=3, sticky="e", **pad)
        self.skp_ref = tk.StringVar(value=f2(SKP_TREF_DEF)); ttk.Entry(self, textvariable=self.skp_ref, width=10).grid(row=1, column=4, **pad)
        ttk.Label(self, text="(×1.25)").grid(row=1, column=5, sticky="w", **pad)
        self.skp_out = tk.StringVar(value="-"); ttk.Label(self, textvariable=self.skp_out).grid(row=1, column=6, **pad)

        # Autocross
        ttk.Label(self, text="Autocross", style="Hdr.TLabel").grid(row=2, column=0, sticky="w", **pad)
        ttk.Label(self, text="t_team [s]").grid(row=2, column=1, sticky="e", **pad)
        self.ax_t = tk.StringVar(); ttk.Entry(self, textvariable=self.ax_t, width=10).grid(row=2, column=2, **pad)
        ttk.Label(self, text="t_ref [s]").grid(row=2, column=3, sticky="e", **pad)
        self.ax_ref = tk.StringVar(value=f2(AX_TREF_DEF)); ttk.Entry(self, textvariable=self.ax_ref, width=10).grid(row=2, column=4, **pad)
        ttk.Label(self, text="(×1.25)").grid(row=2, column=5, sticky="w", **pad)
        self.ax_out = tk.StringVar(value="-"); ttk.Label(self, textvariable=self.ax_out).grid(row=2, column=6, **pad)

        # Endurance
        ttk.Label(self, text="Endurance (t_lap)", style="Hdr.TLabel").grid(row=3, column=0, sticky="w", **pad)
        ttk.Label(self, text="t_lap [s]").grid(row=3, column=1, sticky="e", **pad)
        self.en_t = tk.StringVar(); ttk.Entry(self, textvariable=self.en_t, width=10).grid(row=3, column=2, **pad)
        ttk.Label(self, text="t_ref total [s]").grid(row=3, column=3, sticky="e", **pad)
        self.en_ref = tk.StringVar(value=f2(END_TREF_DEF)); ttk.Entry(self, textvariable=self.en_ref, width=10).grid(row=3, column=4, **pad)
        ttk.Label(self, text="(×1.333)").grid(row=3, column=5, sticky="w", **pad)
        self.en_out = tk.StringVar(value="-"); ttk.Label(self, textvariable=self.en_out).grid(row=3, column=6, **pad)

        # Controls + total
        ttk.Button(self, text="Compute", command=self.compute).grid(row=4, column=0, **pad, sticky="ew")
        ttk.Button(self, text="Clear", command=self.clear).grid(row=4, column=1, **pad, sticky="ew")
        ttk.Label(self, text="Total", style="Hdr.TLabel").grid(row=4, column=5, sticky="e", **pad)
        self.total = tk.StringVar(value="-"); ttk.Label(self, textvariable=self.total, style="Hdr.TLabel").grid(row=4, column=6, sticky="w", **pad)

        for i in range(7): self.grid_columnconfigure(i, weight=1)
        self.bind("<Return>", lambda *_: self.compute())

        # Show startup popup
        self.after(150, lambda: messagebox.showinfo("Reference info", INFO_MESSAGE))

    def _num_or_none(self, s):
        s = s.strip()
        if not s: return None
        try: return float(s)
        except ValueError: raise ValueError("Enter numeric seconds.")

    def _pos_num(self, s, name):
        try:
            v = float(s)
            if v <= 0: raise ValueError
            return v
        except ValueError:
            raise ValueError(f"{name} must be a positive number.")

    def compute(self):
        try:
            # times
            t_acc = self._num_or_none(self.acc_t.get())
            t_skp = self._num_or_none(self.skp_t.get())
            t_ax  = self._num_or_none(self.ax_t.get())
            t_en  = self._num_or_none(self.en_t.get())

            # t_ref -> T_max_new via factors
            acc_ref = self._pos_num(self.acc_ref.get(), "Acceleration t_ref")
            skp_ref = self._pos_num(self.skp_ref.get(), "Skidpad t_ref")
            ax_ref  = self._pos_num(self.ax_ref.get(),  "Autocross t_ref")
            en_ref  = self._pos_num(self.en_ref.get(),  "Endurance t_ref")

            acc_tmax_new = ACC_FACTOR * acc_ref
            skp_tmax_new = SKP_FACTOR * skp_ref
            ax_tmax_new  = AX_FACTOR  * ax_ref
            en_tmax_new  = END_FACTOR * en_ref

            # Pre-scale inputs to emulate new T_max while calling your exact functions
            acc = acceleration_score(scale_for_new_tmax(t_acc, ACC_TMAX_DEF, acc_tmax_new)) if t_acc is not None else 0.0
            skp = skidpad_score     (scale_for_new_tmax(t_skp, SKP_TMAX_DEF, skp_tmax_new)) if t_skp is not None else 0.0
            ax  = autocross_score   (scale_for_new_tmax(t_ax,  AX_TMAX_DEF,  ax_tmax_new )) if t_ax  is not None else 0.0
            en  = endurance_score   (scale_for_new_tmax(t_en,  END_TMAX_DEF, en_tmax_new )) if t_en  is not None else 0.0

            self.acc_out.set(f"Score: {f2(acc)}" if t_acc is not None else "-")
            self.skp_out.set(f"Score: {f2(skp)}" if t_skp is not None else "-")
            self.ax_out.set (f"Score: {f2(ax)}"  if t_ax  is not None else "-")
            self.en_out.set (f"Score: {f2(en)}"  if t_en  is not None else "-")

            total = (acc if t_acc else 0) + (skp if t_skp else 0) + (ax if t_ax else 0) + (en if t_en else 0)
            self.total.set(f2(total) if any(v is not None for v in [t_acc, t_skp, t_ax, t_en]) else "-")
        except ValueError as e:
            messagebox.showerror("Input error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        for var in (self.acc_t, self.skp_t, self.ax_t, self.en_t):
            var.set("")
        for var in (self.acc_out, self.skp_out, self.ax_out, self.en_out):
            var.set("-")
        self.total.set("-")
        self.acc_ref.set(f2(ACC_TREF_DEF))
        self.skp_ref.set(f2(SKP_TREF_DEF))
        self.ax_ref.set (f2(AX_TREF_DEF))
        self.en_ref.set (f2(END_TREF_DEF))

if __name__ == "__main__":
    App().mainloop()
