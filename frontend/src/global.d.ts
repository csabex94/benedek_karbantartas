
export declare global {
    type SidebarSubItem = {
        title: string;
        url: string;
    }

    type SidebarItem = {
        title: string;
        url: string;
        items: SibebarSubItem[]
    }
}