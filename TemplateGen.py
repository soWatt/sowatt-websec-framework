def generate_md_template(company):
    template = f"""
# {company} VDP 

---

## {company} Program Rules
    
Use this section to write about the import parts from the program guidelines. Does the program require you to send a specific header for http requests? Are there certain parts of the application that they absolutely do not want you to test?

## {company} Scope
Put any known assets that are in scope here that you want to test. 

## {company} Notes
Any additional notes as you test go here.
"""
    
    return template

comp = input("What Company's VDP are you testing?\n")

markdown_con = generate_md_template(comp)

with open(f"{comp}VDP.md", "w") as file:
    file.write(markdown_con)

print(f"Template created successfully, please see {comp}VDP.md.")