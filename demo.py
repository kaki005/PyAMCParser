from amc_parser import Viewer, parse_amc, parse_asf

if __name__ == '__main__':
  asf_path = '01.asf'
  amc_path = '01_01.amc'
  joints = parse_asf(asf_path)
  motions = parse_amc(amc_path)
  v = Viewer(joints, motions)
  v.run()
