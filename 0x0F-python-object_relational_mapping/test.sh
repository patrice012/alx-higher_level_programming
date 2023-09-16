#!/usr/bin/bash
# run test case

echo "~~~~~~~~~~ Start testing ~~~~~~~~~"

echo "========== Test task 0 ==========="
sudo ./0-select_states.py root root hbtn_0e_0_usa
echo ""
echo "========== Test task 1 ==========="
sudo ./1-filter_states.py root root hbtn_0e_0_usa
echo ""
echo "========== Test task 2 ==========="
sudo ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
echo ""
echo "========== Test task 3 ==========="
sudo ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
echo ""
echo "========== Test task 4 ==========="
sudo ./4-cities_by_state.py root root hbtn_0e_4_usa
echo ""
echo "========== Test task 5 ==========="
sudo ./5-filter_cities.py root root hbtn_0e_4_usa Texas
sudo ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

echo ""
echo "========== Test task 6 ==========="
sudo ./6-model_state.py root root hbtn_0e_6_usa

echo ""
echo "========== Test task 7 ==========="
sudo ./7-model_state_fetch_all.py root root hbtn_0e_6_usa

echo ""
echo "========== Test task 8 ==========="
sudo ./8-model_state_fetch_first.py root root hbtn_0e_6_usa

echo ""
echo "========== Test task 9 ==========="
sudo ./9-model_state_filter_a.py root root hbtn_0e_6_usa

echo ""
echo "========== Test task 10 ==========="
sudo ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
sudo ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas


echo ""
echo "========== Test task 11 ==========="
sudo ./11-model_state_insert.py root root hbtn_0e_6_usa 
sudo ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 

echo ""
echo "========== Test task 12 ==========="
sudo ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
sudo ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 

echo ""
echo "========== Test task 13 ==========="
sudo ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
sudo ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 

echo ""
echo "========== Test task 14 ==========="
sudo ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa






echo "~~~~~~~~~~~~ Test ending ~~~~~~~~~~~~~~~~~~"