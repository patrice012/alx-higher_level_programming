#!/usr/bin/bash
# migrate data

echo ""
echo "======= migrate hbtn_0e_0_usa ======="
cat 0-select_states.sql | mysql -uroot -p

echo ""
echo "======= migrate hbtn_0e_4_usa ======="
cat 4-cities_by_state.sql | mysql -uroot -p


echo ""
echo "======= migrate hbtn_0e_6_usa ======="
cat 6-model_state.sql | sudo mysql -uroot -p