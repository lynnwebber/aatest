function check_alarm ()
    val = get_value("9.28765.12")
    if val > 16.2 then
        return 1
    else
        return 0
    end
end
