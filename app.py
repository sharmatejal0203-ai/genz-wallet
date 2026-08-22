# =========================================================
# PREMIUM SMART BUDGET + GOAL MANAGER
# =========================================================

st.divider()

# Only show this section on Profile page
if st.session_state.page == "Profile":

    st.subheader("Smart Money Controls")

    # -----------------------------------------------------
    # BUDGET STATUS
    # -----------------------------------------------------

    spent = spending_total()
    limit = max(st.session_state.monthly_limit, 1)
    budget_used = min(spent / limit, 1)

    st.markdown(
        '<div class="card">'
        '<div class="balance-label">MONTHLY BUDGET</div>'
        '<div class="balance" style="font-size:32px;">₹{:,.0f}</div>'
        '<div class="muted">₹{:,.0f} spent of ₹{:,.0f}</div>'
        '</div>'.format(
            spent,
            spent,
            limit
        ),
        unsafe_allow_html=True
    )

    st.progress(budget_used)

    if spent > limit:
        st.error(
            "⚠️ Monthly budget exceeded."
        )
    elif spent >= limit * 0.8:
        st.warning(
            "You're close to your monthly spending limit."
        )
    else:
        st.success(
            "Budget is under control."
        )

    # -----------------------------------------------------
    # CREATE NEW GOAL
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Create a new goal</div>',
        unsafe_allow_html=True
    )

    goal_name = st.text_input(
        "Goal name",
        placeholder="Example: New Phone",
        key="new_goal_name"
    )

    goal_target = st.number_input(
        "Target amount",
        min_value=100.0,
        value=5000.0,
        step=500.0,
        key="new_goal_target"
    )

    if st.button(
        "＋ Create Goal",
        use_container_width=True,
        key="create_new_goal"
    ):

        if not goal_name.strip():

            st.error("Enter a goal name.")

        else:

            st.session_state.goals.append(
                {
                    "name": goal_name.strip(),
                    "target": float(goal_target),
                    "saved": 0.0
                }
            )

            st.success(
                "Goal created successfully."
            )

            st.rerun()

    # -----------------------------------------------------
    # ALL GOALS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Goal overview</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.goals:

        st.info("No goals created yet.")

    else:

        for i, goal in enumerate(
            st.session_state.goals
        ):

            target = max(
                float(goal["target"]),
                1
            )

            saved = float(
                goal["saved"]
            )

            progress = min(
                saved / target,
                1
            )

            st.markdown(
                '<div class="goal">'
                '<div class="goal-title">{}</div>'
                '<div class="goal-money">'
                '₹{:,.0f} / ₹{:,.0f}'
                '</div>'
                '<div class="muted">'
                '{:.0f}% completed'
                '</div>'
                '</div>'.format(
                    goal["name"],
                    saved,
                    target,
                    progress * 100
                ),
                unsafe_allow_html=True
            )

            st.progress(progress)

            g1, g2 = st.columns(2)

            with g1:

                if st.button(
                    "Add Money",
                    use_container_width=True,
                    key="profile_goal_add_" + str(i)
                ):

                    st.session_state[
                        "goal_selected"
                    ] = i

            with g2:

                if st.button(
                    "Delete",
                    use_container_width=True,
                    key="profile_goal_delete_" + str(i)
                ):

                    st.session_state.goals.pop(i)

                    st.rerun()

    # -----------------------------------------------------
    # SELECTED GOAL FUNDING
    # -----------------------------------------------------

    if "goal_selected" in st.session_state:

        selected = st.session_state.goal_selected

        if selected < len(
            st.session_state.goals
        ):

            goal = st.session_state.goals[selected]

            st.markdown(
                "### Add money to " +
                goal["name"]
            )

            goal_amount = st.number_input(
                "Amount",
                min_value=1.0,
                value=100.0,
                step=50.0,
                key="profile_goal_amount"
            )

            if st.button(
                "Confirm Goal Deposit",
                use_container_width=True,
                key="profile_goal_confirm"
            ):

                if goal_amount > st.session_state.balance:

                    st.error(
                        "Insufficient demo balance."
                    )

                else:

                    st.session_state.balance -= goal_amount

                    goal["saved"] += goal_amount

                    add_transaction(
                        goal["name"],
                        "Savings",
                        -goal_amount
                    )

                    st.session_state.notifications.insert(
                        0,
                        "₹{:,.0f} added to {}."
                        .format(
                            goal_amount,
                            goal["name"]
                        )
                    )

                    del st.session_state.goal_selected

                    st.success(
                        "Goal updated."
                    )

                    st.rerun()


# =========================================================
# END
# =========================================================