import sys
sys.path.append('./python-x32/src')
import pythonx32.x32 as x32



mixer = x32.BehringerX32("10.211.55.3")
mixer.ping()
state = mixer.get_state()
print(state)
#
# if args.to_mixer and args.from_mixer:
#     print("Only one of to_mixer and from_mixer must be present at same time.")
#     parser.print_help()
#     sys.exit(1)
# elif args.from_mixer:
#
#     mixer.save_state_to_file(open(args.filename, "wt"), state)
# elif args.to_mixer:
#     read_back_state = mixer.read_state_from_file(inputfile=open(args.filename, "rt"))
#     mixer.set_state(state=read_back_state)
# else:
#     print("One of to_mixer and from_mixer must be present.")
#     parser.print_help()
#     sys.exit(1)