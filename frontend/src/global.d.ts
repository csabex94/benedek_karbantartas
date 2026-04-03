
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
        name: string;
        model: string;
        type: string;
        serialNumber: string;
        ipAddress: string;
        createdAt: string;
        updatedAt: string;
    }

    interface IPrinterService {
        id: number;
        name: string;
        details: ?string;
    }

    interface IUser {
        id: number;
        fullname: string;
        email: string;
    }
}