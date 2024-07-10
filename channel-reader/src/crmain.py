import xair_api


def main():
    kind_id = "X32"
    ip = "10.211.55.3"

    with xair_api.connect(kind_id, ip=ip) as mixer:
        mixer.strip[8].config.name = "TEST"
        mixer.strip[8].mix.on = True
        print(f"{mixer.query("/ch/01/mix/on")[0]}")
        print(
            f"strip 09 ({mixer.strip[8].config.name}) on has been set to {mixer.strip[8].mix.on}"
        )


if __name__ == "__main__":
    main()


#
# mixer = x32.BehringerX32("10.211.55.3")
# mixer.ping()
# state = mixer.get_state()
# print(state)
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