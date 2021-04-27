require "./http/client/digest_auth"

class Http::Client::DigestAuth
  VERSION = {{ `shards version #{__DIR__}`.chomp.stringify }}
end
