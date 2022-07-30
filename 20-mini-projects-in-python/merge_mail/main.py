PLACEHOLDER = "[name]"

with open("input/invited_names.txt") as names_file:
    names_list = [line.strip() for line in names_file]

with open("input/starting_letter.docx") as file:
    text = file.read()

for name in names_list:
    with open(f"output/ready_to_send/letter_for_{name}.docx", mode="w") as invite:
        invite.write(text.replace(PLACEHOLDER, name))
