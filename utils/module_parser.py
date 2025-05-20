def detect_modules(text):
    modules = []

    if "statistic" in text.lower():
        modules.append("statistics")

    if "visualization" in text.lower() or "plot" in text.lower():
        modules.append("visualizations")

    if "venn" in text.lower():
        modules.append("venn")

    if "table" in text.lower():
        modules.append("tables")

    return modules
