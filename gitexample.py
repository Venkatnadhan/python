from dulwich.client import LocalGitClient
from dulwich.repo import Repo

home = os.path.expanduser('~')

local_folder = os.path.join(home, 'temp/local'
local = Repo(local_folder)

remote = os.path.join(home, 'temp/remote')

wants = local.object_store.determine_wants_all
remote_refs = LocalGitClient().fetch(remote, local, wants)
local_refs = LocalGitClient().get_refs(local_folder)

print(remote_refs)
print(local_refs)