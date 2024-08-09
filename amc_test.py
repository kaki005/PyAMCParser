from amcparser import Viewer, amc_to_tensor, parse_amc, parse_asf

if __name__ == "__main__":
    asf_path = "data/01.asf"
    amc_path = "data/01_01.amc"
    joints = parse_asf(asf_path)
    motions = parse_amc(amc_path)
    tensor = amc_to_tensor(motions, joints)
    print("tensor =", tensor.shape)
    joints["root"].draw()
    v = Viewer(joints)
    v.run_with_tensor(tensor)
