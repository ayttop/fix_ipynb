import nbformat

input_file = "suc_turboquan_a.ipynb"
output_file = "fixed_final.ipynb"

nb = nbformat.read(input_file, as_version=nbformat.NO_CONVERT)

# ✅ حذف widgets من metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# ✅ تنظيف outputs جزئي (بس widgets)
for cell in nb.cells:
    if "outputs" in cell:
        new_outputs = []
        for output in cell["outputs"]:
            if "data" in output:
                # حذف widget فقط
                if "application/vnd.jupyter.widget-view+json" in output["data"]:
                    continue
            new_outputs.append(output)
        cell["outputs"] = new_outputs

nbformat.write(nb, output_file)

print("✅ تم إصلاح النوتبوك مع الحفاظ على النتائج")