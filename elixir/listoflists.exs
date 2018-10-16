defmodule WeatherHistory do

  def test_data do
    [
      #time,pod,temp,rainfall
      [0800,2341,56.5,0.001],
      [0900,2341,68.2,0.2],
      [1000,2341,80.3,0.001],
      [1100,2341,83.5,0.45],
      [1200,2341,90.7,0.001],
      [0800,2355,56.5,0.001],
      [0900,2355,68.2,0.2],
      [1000,2355,80.3,0.001],
      [1100,2355,83.5,0.45],
      [1200,2355,90.7,0.001],
      [0800,2388,56.5,0.001],
      [0900,2388,68.2,0.2],
      [1000,2388,80.3,0.001],
      [1100,2388,83.5,0.45],
      [1200,2388,90.7,0.001]
    ]
  end


  def for_pod([], _target_pod) do
    []
  end
  def for_pod([ head=[_, target_pod, _, _] | tail], target_pod) do
    [ head | for_pod(tail, target_pod) ]
  end
  def for_pod([ _ | tail], target_pod) do
    for_pod(tail, target_pod)
  end
end
