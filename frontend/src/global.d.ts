
export declare global {

    interface ISidebarSubItem {
        title: string;
        url: string;
        name: ?string;
    }

    interface ISidebarItem {
        title: string;
        url: string;
        items: SibebarSubItem[]
    }

    interface IPrinter {
        id: number;
        model: string;
        ipAddress: string;
    }

}