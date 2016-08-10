defmodule Greeter do
    def howdy(name), do: "howdy, " <> name
    def heythere(name), do: "hey there " <> name <> ", how you doing?"
end


defmodule Length do
    def of([]), do: 0
    def of([_|rest]), do: 1+of(rest)
end
