import typer
import pyfiglet
import inquirer
from yaspin import yaspin,spinners
from rich import print
import time
import ip_works


with yaspin(spinners.Spinners.line, text=" IP LookUP loading ... ", color="yellow"):
    time.sleep(1.2)


def main(
        IP_Address: str = typer.Option(..., prompt=True)
):

    options = [inquirer.List("ip_info_choices", message="What type of information you want?",
                             choices=["IP Class", "Net & Host Info", "All"])]

    choices = inquirer.prompt(options)
    if choices["ip_info_choices"] == "IP Class":
        print(f" IP Address {IP_Address} is in Class {ip_works.ip_Class_Info(IP_Address)}")
    if choices["ip_info_choices"] == "Net & Host Info":
        print(ip_works.ip_host_and_net_info(ip_works.ip_Class_Info(IP_Address), IP_Address))
    if choices["ip_info_choices"] == "All":
        print("[bright_blue]Feature[/bright_blue] : Coming soon ...")

    print("\n\n❤️ [bright_green] Thank You for using IP LookUP[bright_green] \n More Featurs Coming soon\n\n\n")

    typer.pause()


if __name__ == '__main__':
    f = pyfiglet.figlet_format("  \"  IP Look UP  \"", font="slant")
    print(f)
    print("😻[bold yellow] Welcome to IP LookUp... [/bold yellow]\n\n\n")
    print(" Enter your [bright_cyan]IP Address[/bright_cyan] to get [cyan]info[/cyan] about [red]:[/red] \n\n like this ..."
          " \n\n 👉 192.168.18.1 \nor\n 👉 192.168.18.1/25\n\n\n")
    typer.run(main)





