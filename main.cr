# require "option_parser"
require "json"

def run_cmd(cmd, args)
  stdout = IO::Memory.new
  stderr = IO::Memory.new
  status = Process.run(cmd, args: args, output: stdout, error: stderr)
  if status.success?
    {status.exit_code, stdout.to_s}
  else
    {status.exit_code, stderr.to_s}
  end
end


def auth(token)
  resp = run_cmd("curl", %( -X GET "https://pat.doggo.ninja/v1/me" -H "accept: application/json" -H "Authorization: Bearer #{token}"))
  return JSON.parse resp
end


puts auth(ENV["TOKEN"])