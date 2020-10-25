import subprocess

# First, convert mcrl2 model to lps
# /usr/bin/mcrl22lps --check-only airlock_project/airlock_project_spec.mcrl2 /tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_lps.lps --lin-method=regular --rewriter=jitty --verbose
subprocess.Popen(["/usr/bin/mcrl22lps", "--check-only", "airlock_project/airlock_project_spec.mcrl2", "airlock_project/temp/temp_airlock_project_lps.lps", "--lin-method=regular", "--rewriter=jitty", "--verbose"]).communicate()
# ["/usr/bin/mcrl22lps", "airlock_project/airlock_project_spec.mcrl2", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_lps.lps", "--lin-method=regular", "--rewriter=jitty", "--verbose"]
subprocess.Popen(["/usr/bin/mcrl22lps", "airlock_project/airlock_project_spec.mcrl2", "airlock_project/temp/temp_airlock_project_lps.lps", "--lin-method=regular", "--rewriter=jitty", "--verbose"]).communicate()

requirements = [
    # "No deadlocks",
    # "FR01",
    # "FR02",
    # "FR03",
    # "FR04",
    # "FR05",
    # "FR06",
    # "FR07",
    # "FR08",
    # "FR09",
    # "FR10",
    # "FR11",
    # "FR12",
    # "FR13",
    # "FR14",
    # "FR15",
    "FR14a",
    "FR14b",
    "FR14c",
    "FR14d",
    "FR14e",
    "FR14f",
]

outputs = {}
for req in requirements:
    # Conert lps to pbes
    # ["/usr/bin/lps2pbes", "--check-only", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_lps.lps", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_No deadlocks_pbes.pbes", "--formula=airlock_project/properties/No deadlocks.mcf", "--out=pbes", "--verbose"]
    subprocess.Popen(["/usr/bin/lps2pbes", "--check-only", "airlock_project/temp/temp_airlock_project_lps.lps", f"airlock_project/temp/temp_airlock_project_{req}_pbes.pbes", f"--formula=airlock_project/properties/{req}.mcf", "--out=pbes", "--verbose"]).communicate()
    # Add formula to pbes
    # ["/usr/bin/lps2pbes", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_lps.lps", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_No deadlocks_pbes.pbes", "--formula=airlock_project/properties/No deadlocks.mcf", "--out=pbes", "--verbose"]
    subprocess.Popen(["/usr/bin/lps2pbes", "airlock_project/temp/temp_airlock_project_lps.lps", f"airlock_project/temp/temp_airlock_project_{req}_pbes.pbes", f"--formula=airlock_project/properties/{req}.mcf", "--out=pbes", "--verbose"]).communicate()

for req in requirements:
    # Solve the pbes
    # ["/usr/bin/pbessolve", "/tmp/mcrl2ide-HOEOec/84882e77ee78c28546532b2f7f6a17fa_airlock_project_No deadlocks_pbes.pbes", "--in=pbes", "--rewriter=jitty", "--search-strategy=breadth-first", "--solve-strategy=0", "--verbose"]
    # output = subprocess.Popen(["/usr/bin/pbessolve", f"temp_airlock_project_{req}_pbes.pbes", "--in=pbes", "--rewriter=jittyc", "--search-strategy=breadth-first", "--solve-strategy=0", "--verbose"])
    # outputs[req] = output
    ret, _ = subprocess.Popen(["/usr/bin/pbessolve", f"airlock_project/temp/temp_airlock_project_{req}_pbes.pbes", "--in=pbes", "--rewriter=jittyc", "--search-strategy=breadth-first", "--solve-strategy=0", "--verbose"], stdout=subprocess.PIPE).communicate()
    outputs[req] = ret


print("\nRESULTS")
print(outputs)
# for req in requirements:
#     print(f"{req}" + outputs[req])
