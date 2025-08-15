import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class LeadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relatório de Leads")
        self.root.geometry("600x500")
        
        
        self.file_path = tk.StringVar()
        self.report_text = tk.StringVar()
        
        
        tk.Label(root, text="Selecione o arquivo CSV:").pack(pady=5)
        tk.Entry(root, textvariable=self.file_path, width=50).pack(pady=5)
        tk.Button(root, text="Procurar arquivo", command=self.select_file).pack(pady=5)
        tk.Button(root, text="Processar Leads", command=self.process_file).pack(pady=10)
        
        tk.Label(root, text="Resumo do Relatório:", font=("Arial", 12, "bold")).pack(pady=5)
        self.text_area = tk.Text(root, height=20, width=70)
        self.text_area.pack(pady=5)
        
    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.file_path.set(path)
        
    def process_file(self):
        path = self.file_path.get()
        if not path:
            messagebox.showerror("Erro", "Selecione um arquivo CSV primeiro!")
            return
        
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                counter = -1
                creatives_dict = {}
                city = None
                
                for row in reader:    
                    city = row[3]
                    creative = row[6]
                    if row[6] != "Lead Manual" and "Orgânico" not in row[6]:
                        counter += 1
                    
                    if "creative:" in creative:
                        creative_name = creative.split("creative:")[1].split("/")[0].strip()
                        if creative_name not in creatives_dict:
                            creatives_dict[creative_name] = 0
                        creatives_dict[creative_name] += 1
                
                
                report_lines = [
                    "="*50,
                    f"Cidade: {city}",
                    f"Total de Leads: {counter}",
                    "="*50,
                    f"{'Criativo':<30} | {'Quantidade':>10}",
                    "-"*50
                ]
                
                for creative, count in creatives_dict.items():
                    report_lines.append(f"{creative:<30} | {count:>10}")
                
                report_lines.append("="*50)
                
                
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, "\n".join(report_lines))
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar arquivo:\n{e}")

root = tk.Tk()
app = LeadApp(root)
root.mainloop()
