import sys
import nbformat

def clean_notebook(input_file, output_file):
    nb = nbformat.read(input_file, as_version=4)

    # حذف widgets metadata
    nb.metadata.pop("widgets", None)

    # تنظيف widget outputs فقط
    for cell in nb.cells:
        if "outputs" in cell:
            cell["outputs"] = [
                o for o in cell["outputs"]
                if not (
                    "data" in o and
                    "application/vnd.jupyter.widget-view+json" in o["data"]
                )
            ]

    nbformat.write(nb, output_file)
    print("✅ cleaned:", output_file)


# 🔥 قراءة المسار من command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ استخدم:")
        print("python fix_nb.py /path/to/file.ipynb")
        sys.exit(1)

    input_file = sys.argv[1]

    # اسم الملف الناتج تلقائي
    output_file = input_file.replace(".ipynb", "_fixed.ipynb")

    clean_notebook(input_file, output_file)