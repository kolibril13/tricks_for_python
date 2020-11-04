import httpimport
with httpimport.remote_repo(['hello'],"https://gist.githubusercontent.com/kolibril13/fc84c6940a8aeab8071c5d54d4df3a7b/raw/bedba99860d301fdc20edac5291b52359a46d1e3/"):
    import hello
hello.hello()
