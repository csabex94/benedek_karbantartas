import { reactive, computed } from 'vue';

type TInitialState = {
    currentUser: IUser | null | undefined
}

const INITIAL_STATE: TInitialState = reactive({
    currentUser: null
});

const getCurrentUser = computed(() => {
    return INITIAL_STATE.currentUser
});

const setCurrentUser = (user: IUser) => {
    INITIAL_STATE.currentUser = user;
}

export function useAuth() {
    return {
        getCurrentUser: getCurrentUser,
        setCurrentUser: setCurrentUser
    }
}