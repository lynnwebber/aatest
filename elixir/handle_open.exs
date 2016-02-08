handle_open = fn
    {:ok,file} -> "First Line: #{IO.read(file,:line)}"
    {_,error} -> "Error: #{:file.format_error(error)}"
end
IO.puts handle_open.(File.open("/Users/lynn/Desktop/rtu_channel_work.xml"))
IO.puts handle_open.(File.open("whoknows.txt"))
